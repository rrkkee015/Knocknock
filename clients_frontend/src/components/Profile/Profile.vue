<template>
	<div>
		<div class="mx-10">
			<v-text-field 
				outlined
				:value=nickname
				clearable
				class="profile-textfield"
			>
			</v-text-field>
			<v-btn 
				text 
				block 
				class="font-weight-bold"
			>
				수정
			</v-btn>
		</div>
		<div class="divide-box"></div>
		<div class="px-8">
			<v-row>
				<v-col 
					cols="4"
					class="font-weight-bold"
				>
					이메일
				</v-col>
				<v-col 
					cols="8"
					class="charcoal--text"	
				>
					{{ email }}
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="4"
					class="font-weight-bold"
				>
					비밀번호
				</v-col>
				<v-col 
					cols="8"
					class="py-0 d-flex"	
				>
					<v-text-field 
						filled
						dense
						single-line
						type="password"
						placeholder="6자 이상"
					>
					</v-text-field>
					<v-btn 
						depressed 
						tile 
						dark 
						color="grey darken-1"
						class="profile-btn ml-2"
					>
						변경
					</v-btn>
				</v-col>
			</v-row>
		</div>
		<div class="positon-bottom">
			<v-btn 
				text
				@click="logOut()"
				class="charcoal--text"
			>
				로그아웃
			</v-btn>
			<v-btn 
				text
				class="charcoal--text"
			>
				회원탈퇴
			</v-btn>
		</div>
	</div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
import router from '../../router'

export default {
	computed: {
		...mapState('auth', ['email', 'nickname', 'err'])
	},
	methods: {
    ...mapMutations('auth', ['initError', 'logInCondition', 'initEmail']),
		...mapActions('auth', ['signOut']),
		async logOut () {
			await this.signOut()
			if (!this.err) {
				console.log('로그아웃 성공')
				router.push('/')
				this.logInCondition()
				this.initEmail()
			} else {
				console.log('로그아웃 실패')
				this.initError()
			}
		}
	},
}
</script>

<style scoped>
.divide-box {
	width: 100%; 
	height: 30px; 
	background-color: whitesmoke;
	margin: 20px 0;
}
.charcoal--text {
	color: rgb(102, 102, 102);
}
.profile-textfield {
	height: 60px;
	margin-top: 24px;
}
.profile-btn {
	height: 40px !important;
}
.positon-bottom {
	position: absolute;
	bottom: 5px;
	right: 5px;
}
</style>