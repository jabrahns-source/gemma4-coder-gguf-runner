# ═══════════════════════════════════════════════════════════════════════════════
# Gemma 4 12B Coder — Docker Runtime
# ═══════════════════════════════════════════════════════════════════════════════

# Stage 1: Build llama.cpp with CUDA support
FROM nvidia/cuda:12.4.1-devel-ubuntu22.04 AS builder

RUN apt-get update && apt-get install -y \
    git \
    cmake \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src
RUN git clone --depth 1 https://github.com/ggerganov/llama.cpp.git

WORKDIR /src/llama.cpp/build
RUN cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DGGML_CUDA=ON \
    && make -j$(nproc)

# Stage 2: Runtime
FROM nvidia/cuda:12.4.1-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy built binaries
COPY --from=builder /src/llama.cpp/build/bin/llama-server /usr/local/bin/llama-server
COPY --from=builder /src/llama.cpp/build/bin/llama-cli /usr/local/bin/llama-cli

# Copy scripts and config
COPY scripts/ /app/scripts/
COPY config/ /app/config/

WORKDIR /app

# Expose API port
EXPOSE 18080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:18080/health || exit 1

# Default: run server with model from mounted volume
ENV MODELS_DIR=/app/models
ENV LLAMA_SERVER=/usr/local/bin/llama-server
ENV HOST=0.0.0.0
ENV PORT=18080
ENV CTX_SIZE=16384
ENV N_GPU_LAYERS=99
ENV TEMP=1.0
ENV TOP_P=0.95
ENV TOP_K=64
ENV CACHE_TYPE_K=q8_0
ENV CACHE_TYPE_V=q8_0
ENV BATCH_SIZE=2048
ENV UBATCH_SIZE=512

ENTRYPOINT ["/app/scripts/start-server.sh"]
