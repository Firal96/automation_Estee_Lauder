node{
    stage('Preparation') {
        checkout scm
    }
    stage('test') {
        def myTestContainer = docker.image('fsfe/pipenv:bitnami-3.8')
        myTestContainer.inside {
            sh 'pipenv install'
            sh 'pipenv run python -m pytest'
        }
    }
}
