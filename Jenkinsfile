pipeline {
    agent any

    environment {
        GOOGLE_MAPS_API_KEY = credentials('GOOGLE_MAPS_API_KEY')
    }

    stages {
        // Clean workspace to avoid conflicts
        stage('Clean Workspace') {
            steps {
                cleanWs()  // Clean Jenkins workspace
            }
        }

        // Build Stage
        stage('Build') {
            steps {
                script {
                    echo 'Setting up virtual environment and installing dependencies...'
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'

                    // Debugging: List installed packages
                    echo 'Listing installed packages...'
                    sh '. venv/bin/activate && pip list'
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

        // Further stages
        stage('Deploy to Staging') {
            steps {
                script {
                    echo 'Deploying to staging environment...'
                    // Deployment steps
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    echo 'Deploying to production environment...'
                    // Deployment steps for production
                }
            }
        }

        stage('Monitoring and Alerting') {
            steps {
                script {
                    echo 'Setting up monitoring and alerting...'
                    // Monitoring steps
                }
            }
        }
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
