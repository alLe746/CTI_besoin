FROM python
WORKDIR /interface
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN django-admin startproject pythonui
ADD pythonui/interface /interface/pythonui/interface
COPY pythonui/pythonui/urls.py ./pythonui/pythonui
COPY pythonui/pythonui/settings.py ./pythonui/pythonui
COPY pythonui/Besoin_recup.docx ./pythonui
WORKDIR ./pythonui
RUN python manage.py migrate
EXPOSE 8000
CMD ["python","manage.py","runserver","--noreload","0.0.0.0:8000"]
