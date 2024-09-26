pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        // Debugging step: List files in the Jenkins workspace
        stage('Check Files') {
            steps {
                script {
                    echo 'Listing files in Jenkins workspace...'
                    sh 'ls -la'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Setting up virtual environment and installing dependencies...'
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running Django unit tests...'
                    sh '. venv/bin/activate && python manage.py test'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
