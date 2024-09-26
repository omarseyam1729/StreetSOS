pipeline {
    agent any

    options {
        // Clean the workspace before checking out code
        cleanBeforeCheckout()
    }

    environment {
        GOOGLE_MAPS_API_KEY = credentials('GOOGLE_MAPS_API_KEY')
    }

    stages {
        // Build Stage
        stage('Build') {
            steps {
                script {
                    echo 'Setting up virtual environment and installing dependencies...'
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        // Test Stage
        stage('Test') {
            steps {
                script {
                    echo 'Running Django unit tests...'
                    sh '. venv/bin/activate && python manage.py test'
                }
            }
        }

        // Continue with other stages...
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
