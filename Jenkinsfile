node{
    stage('Preparation') {
        checkout scm
    }
    stage('test') {
        def myTestContainer = docker.image('fsfe/pipenv')
        myTestContainer.inside {
            sh 'pipenv install'
            sh 'pipenv run python -m pytest'
        }
    }
}
