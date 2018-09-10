import Vue from 'vue'
import Router from 'vue-router'
import CompetitionView from '../components/main/CompetitionView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name : 'CompetitionView',
      component: CompetitionView
      //추후 메인페이지 확립 시, path 수정 => /CompetitionView
    }
  ]
})
