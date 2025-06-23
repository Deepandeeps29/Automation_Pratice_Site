pipeline {
    agent any

    environment {
        REPORT_FILE = "report.html"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Deepandeeps29/Automation_Pratice_Site.git'
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

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', onlyIfSuccessful: false
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Login Test Report'
                ])
            }
        }
    }

    post {
        always {
            emailext (
                subject: "Selenium Login Test Report: ${currentBuild.currentResult}",
                body: """<p>Build Result: ${currentBuild.currentResult}</p>
                         <p>View Report: <a href="${BUILD_URL}HTML_20Report/">Click here</a></p>""",
                attachLog: true,
                attachmentsPattern: 'report.html',
                to: 'deepanvinayagam1411@gmail.com'
            )
        }
    }
}
