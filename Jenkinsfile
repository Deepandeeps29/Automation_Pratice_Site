pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest tests/test_login.py --html=report.html --self-contained-html'
            }
        }

        stage('Send Email Report via Python') {
            steps {
                bat 'python send_email.py'
            }
        }
    }
}
