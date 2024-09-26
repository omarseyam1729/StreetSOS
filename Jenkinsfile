pipeline {
    agent any

    // Skip the default automatic SCM checkout
    options {
        skipDefaultCheckout(true)
    }

    environment {
        GOOGLE_MAPS_API_KEY = credentials('GOOGLE_MAPS_API_KEY')
    }

    stages {
        // Stage to clean workspace and checkout code
        stage('Clean and Checkout') {
            steps {
                // Clean the workspace
                cleanWs()

                // Checkout the code from SCM
                checkout scm
            }
        }

        // Optional: Verify that files are present
        stage('Verify Files') {
            steps {
                echo 'Listing files in Jenkins workspace after checkout...'
                sh 'ls -la'
            }
        }

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

        // Continue with other stages (Deploy, Release, Monitoring)...
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
