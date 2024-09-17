pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'Cloud Ideathon'
        DOCKER_CREDENTIALS_ID = 'dockerhub_credentials'  // Set up DockerHub credentials in Jenkins
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-repo/crop-recommendation-system.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Test Docker Image') {
            steps {
                script {
                    // Test your Docker container here
                    docker.image(DOCKER_IMAGE).inside {
                        sh 'pytest tests/'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDENTIALS_ID) {
                        docker.image(DOCKER_IMAGE).push('latest')
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Define your deployment steps (to cloud, server, etc.)
                echo 'Deploying the application...'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
