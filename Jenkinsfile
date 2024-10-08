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
                cleanWs() // Clean the workspace

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

        // Stage for Deploying to AWS EC2
        stage('Deploy to AWS EC2') {
            steps {
                script {
                    echo 'Deploying application to AWS EC2 instance...'
                withCredentials([sshUserPrivateKey(credentialsId: '37ceb940-2e7b-4639-8ce6-19e988e124f4', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER')]) {
                sh """
                ssh -o StrictHostKeyChecking=no -i \$SSH_KEY \$SSH_USER@3.25.171.134 << EOF
                cd /path/to/your/django/project/StreetSOS
                git pull origin main
                source venv/bin/activate
                pip install -r requirements.txt
                python manage.py migrate
                python manage.py collectstatic --noinput
                sudo systemctl restart gunicorn
                EOF
                """
        }

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
