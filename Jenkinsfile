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
            emailext(
                subject: "Jenkins Automation Test Report - ${currentBuild.currentResult}",
                body: """<p>Hi Team,</p>
                         <p>The Jenkins job <b>${env.JOB_NAME} #${env.BUILD_NUMBER}</b> has completed with status: <b>${currentBuild.currentResult}</b>.</p>
                         <p><a href="${env.BUILD_URL}Login_20Test_20Report">Click here to view the HTML Test Report</a></p>
                         <br><p>Thanks,<br>Jenkins</p>""",
                mimeType: 'text/html',
                to: 'deepanvinayagam1411@gmail.com'
            )
        }
    }
}
