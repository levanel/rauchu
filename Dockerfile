# Start with a standard Python environment
FROM python:3.10

# Set the working directory inside the container
WORKDIR /code

# Copy your requirements file and install the libraries
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy all your actual code into the container
COPY . /code

# Expose the port Hugging Face uses
EXPOSE 7860

# Command to run your FastAPI app on port 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
