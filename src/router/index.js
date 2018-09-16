import Vue from 'vue'
import Router from 'vue-router'
import Main from '../components/main/Main'
import Competition from '../components/competition/Competition'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name : 'main',
      component: Main
      //추후 메인페이지 확립 시, path 수정 => /CompetitionView
    },
    {
      path: '/competition',
      name: 'competition',
      component: Competition 
    }
  ]
})
