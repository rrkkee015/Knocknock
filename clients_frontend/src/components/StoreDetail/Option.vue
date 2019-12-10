<template>
	<div class="px-5 py-5">
		<div>
			<p class="notice-title">소개말</p>
			<div 
				v-if="store.description"
				class="notice-content"
			>
				<div v-show="descActive">
					<span>{{ descSummary }}</span>
					<v-btn 
						@click="descActive=false"
						icon
						class="desc-btn"
					>
						<v-icon v-if="isSliced">mdi-chevron-down</v-icon>
					</v-btn>
				</div>
				<div v-show="!descActive">
					<span>{{ store.description }}</span>
					<v-btn 
						v-if="isSliced"
						@click="descActive=true"
						icon
						class="desc-btn"
					>
						<v-icon>mdi-chevron-up</v-icon>
					</v-btn>
				</div>
			</div>
			<p 
				v-else
				class="none-content"
			>	
				소개말이 없어요.
			</p>
		</div>

		<div class="mt-2">
			<p class="notice-title">영업 정보</p>
			<div
				v-if="store.options.length"
				class="notice-content"	
			>
				<div
					v-for="(option, idx) in store.options"
					:key="idx"
					class="d-inline"
				>
					<span>{{ option }}</span>
					<span v-if="idx !== store.options.length -1">, </span>
				</div>
			</div>
			<p
				v-else
				class="none-content"
			>
				상세정보가 없어요.
			</p>
		</div>

		<div class="mt-10">
			<p 
				v-if="store.updatedAt" 
				class="notice-content"
			>
				{{ store.updatedAt }} 수정
			</p>
		</div>
	</div>
</template>

<script>
import { mapState } from 'vuex'

export default {
	data() {
		return {
			isSliced: true,
			descActive: true
		}
	},
	computed: {
		...mapState('store', ['store']),
		descSummary () {
			if (this.store.description.length > 75) {
				return this.store.description.slice(0, 75) + '...'
			} else {
				this.isSliced = false
				return this.store.description
			}
		}
	},
}
</script>

<style scoped>
.notice-title {
	margin-bottom: 0;
	font-weight: 600;
}
.notice-content {
	font-size: 15px;
	color: rgb(102, 102, 102);
}
.none-content {
	font-size: 14px;
	color: grey;
}
.desc-btn {
	width: 24px;
	height: 24px;
	padding-left: 20px;
}
</style>