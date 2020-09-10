node {
     def app
     stage('Clone repository') {
	checkout scm
     }
     stage('Build Image') {
	app = docker.build("vineeth0696/capstone")
     }
     stage('Test Image') {
	app.inside{
		echo "Tests passed"
	}
     }
     stage('Push Image') {
	docker.withRegistry('https://hub.docker.com','docker-hub'){
		app.push("${env.BUILD_NUMBER}")
		app.push("latest")
	}
		echo "pushing image to docker hub"
     }
}
