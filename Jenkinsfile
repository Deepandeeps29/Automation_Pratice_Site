pipeline {
    agent any

    stages {
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
                archiveArtifacts artifacts: 'report.html', fingerprint: true
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
                subject: "Test Report - ${currentBuild.fullDisplayName} - ${currentBuild.currentResult}",
                body: """
                    <p>Test has completed with result: ${currentBuild.currentResult}</p>
                    <p><a href="${BUILD_URL}HTML_20Report/">Click here to view report</a></p>
                """,
                attachLog: true,
                attachmentsPattern: 'report.html',
                mimeType: 'text/html',
                to: 'your_email@gmail.com'
        )
    }
}

}
