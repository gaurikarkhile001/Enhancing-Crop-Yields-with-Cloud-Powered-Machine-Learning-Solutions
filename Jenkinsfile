pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'dockerhub-crop-recommendation-system/cloud-ideathon'  // Use your actual DockerHub username
        DOCKER_CREDENTIALS_ID = 'dockerhub_credentials'  // Make sure credentials are set in Jenkins
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the code from your GitHub repository
                git 'https://github.com/gaurikarkhile001/Enhancing-Crop-Yields-with-Cloud-Powered-Machine-Learning-Solutions.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Test Docker Image') {
            steps {
                script {
                    // Assuming you have tests set up inside the Docker container
                    docker.image("${DOCKER_IMAGE}").inside {
                        // Run pytest or any other testing framework you have
                        sh 'pytest tests/'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push Docker image to DockerHub
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDENTIALS_ID) {
                        docker.image("${DOCKER_IMAGE}").push('latest')
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Deployment step (adjust based on your deployment strategy)
                    echo 'Deploying the application...'
                    // Add your deployment logic here
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace after build
            cleanWs()
        }
    }
}
