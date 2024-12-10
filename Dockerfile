FROM python:3.9-slim

ENV ACCEPT_EULA=Y
RUN apt-get update -y && apt-get update \
  && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends --allow-unauthenticated msodbcsql17 mssql-tools \
  && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
  && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc \
  && apt-get install -y --no-install-recommends --allow-unauthenticated msodbcsql17 mssql-tools

RUN pip install pyodbc
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


RUN apt-get -y clean

EXPOSE 8000

CMD ["python", "app.py"]

# Docker Image: mxfrgsn/comp2001_cw2
# GitHub Repository: https://github.com/MxFrgsn/COMP2001-CW2
# docker run -p 8000:8000 mxfrgsn/comp2001_cw2