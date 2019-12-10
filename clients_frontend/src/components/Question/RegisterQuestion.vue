<template>
	<v-container>
		<p class="font-headline">1:1 문의하기</p>
		<div class="px-8">
			<v-row>
				<v-col 
					cols="3"
					class="font-weight-medium"
				>
					이름
				</v-col>
				<v-col cols="9">
					<v-text-field 
						outlined
						dense
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col 
					cols="3"
					class="font-weight-medium"
				>
					이메일
				</v-col>
				<v-col cols="9">
					<v-text-field 
						outlined
						dense
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col 
					cols="3"
					class="font-weight-medium"
				>
					상담분류
				</v-col>
				<v-col cols="9">
					<v-select
						v-model="select"
						:items="items"
						:rules="[v => !!v || 'Item is required']"
						required
						outlined
						dense
					></v-select>
				</v-col>
			</v-row>
			<v-row>
				<v-col 
					cols="3"
					class="font-weight-medium"
				>
					제목
				</v-col>
				<v-col cols="9">
					<v-text-field 
						outlined
						dense
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col 
					cols="3"
					class="font-weight-medium"
				>
					문의내용
				</v-col>
				<v-col cols="9">
					<v-textarea 
						outlined
						dense
					></v-textarea>
				</v-col>
			</v-row>
			<div class="d-flex justify-center">
				<v-btn 
					@click="goTo('main')"
					x-large
					text
				>
					취소
				</v-btn>
				<v-btn 
					@click="goTo('main')"
					x-large
					text 
					color="primary"
				>
					작성완료
				</v-btn>
			</div>
		</div>
	</v-container>
</template>

<script>
import router from '../../router'
export default {
	data() {
		return {
			select: '선택안함',
			items: ['선택안함', '오류문의', '회원정보문의', '리뷰문의', '제휴문의', '업소정보문의', '이벤트', '기타']
		}
	},
	methods: {
		goTo(path) {
			router.push({ name: path })
		}
	}
}
</script>

<style scoped>
.font-headline {
  font-size: 24px;
  font-weight: 700;
}
.col {
	padding: 0;
}
</style>