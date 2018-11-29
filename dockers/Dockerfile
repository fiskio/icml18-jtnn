FROM gitlab.beno.ai:4567/bic/tools/cuda-images:ubuntu-18.04-rdkit-python3

# python deps
COPY requirements.txt /tmp
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Add the source code
RUN mkdir -p /app
ADD . /app

# RUN python setup.py install

# Launch inside the folder
WORKDIR /app/
