FROM python:3.10-slim

# Install system dependencies for RDKit
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      python3-dev \
      wget \
      ca-certificates \
      git \
      libglib2.0-0 \
      libsm6 \
      libxrender1 \
      libxext6 && \
    rm -rf /var/lib/apt/lists/*

# Install RDKit via conda (using miniforge)
RUN wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O Miniforge3.sh && \
    bash Miniforge3.sh -b -p /opt/conda && \
    rm Miniforge3.sh
ENV PATH=/opt/conda/bin:$PATH

# Create environment and install RDKit, AiZynthFinder, FastAPI, uvicorn
RUN conda create -n chemgpt-se python=3.10 rdkit=2023.03.2 -c conda-forge && \
    /opt/conda/bin/conda run -n chemgpt-se pip install fastapi uvicorn aizynthfinder==4.3.2 && \
    conda clean -afy

ENV CONDA_DEFAULT_ENV=chemgpt-se

WORKDIR /app
COPY . .

# 🔥 Expose port 8000 (to match Railway)
EXPOSE 8000

# 🔥 Run with Uvicorn on port 8000 (matches FastAPI & Railway)
CMD ["/opt/conda/bin/conda", "run", "-n", "chemgpt-se", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
