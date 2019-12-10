import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '../pages/MainPage'
import AuthPage from '../pages/AuthPage'
import TermsOfUsePage from '../pages/TermsOfUsePage'
import StoreDetailPage from '../pages/StoreDetailPage'
import ProfilePage from '../pages/ProfilePage'
import ManageReviewsPage from '../pages/ManageReviewsPage'
import ModifyReviewPage from '../pages/ModifyReviewPage'
import NoticePage from '../pages/NoticePage'
import QuestionPage from '../pages/QuestionPage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    { path: '/', name: 'main', component: MainPage },
    { path: '/auth', name: 'auth', component: AuthPage },
		{ path: '/termsofuse', name: 'termsofuse', component: TermsOfUsePage },
		{ path: '/notice', name: 'notice', component: NoticePage },
		{ path: '/question', name: 'question', component: QuestionPage },

    { path: '/store/:storeId', name: 'store-detail', component: StoreDetailPage },

    { path: '/profile', name: 'profile', component: ProfilePage },

		{ path: '/reviews', name: 'reviews', component: ManageReviewsPage },
		{ path: '/reviews/:reviewId', name: 'modify-review', component: ModifyReviewPage }
  ]
})
