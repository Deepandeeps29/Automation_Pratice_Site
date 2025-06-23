pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-token',
                url: 'https://github.com/Deepandeeps29/Automation_Pratice_Site.git',
                branch: 'main'
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
