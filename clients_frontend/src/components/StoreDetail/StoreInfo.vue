<template>
	<div>
		<v-tabs
			v-model="tab"
			background-color="transparent"
			grow
		>
			<v-tab
				v-for="item in items"
				:key="item"
			>
				{{ item }}
			</v-tab>
		</v-tabs>

		<v-tabs-items v-model="tab">
			<v-tab-item>
				<v-card flat>
					<Option class="height-350" />
				</v-card>
			</v-tab-item>
			<v-tab-item>
				<v-card flat>
					<Menu class="height-350" />
				</v-card>
			</v-tab-item>
			<v-tab-item>
				<v-card flat>
					<Location class="height-350" />
				</v-card>
			</v-tab-item>
			<v-tab-item>
				<v-card flat>
					<Review class="height-350" />
				</v-card>
			</v-tab-item>
		</v-tabs-items>
	</div>
</template>

<script>
import Option from './Option'
import Menu from './Menu'
import Location from './Location'
import Review from './Review'

export default {
	data() {
		return {
			tab: null,
			items: [
				'정보', '메뉴', '지도', '리뷰'
			]
		}
	},
	components: {
		Option,
		Menu,
		Location,
		Review
	}
}
</script>

<style scoped>
.height-350 {
	height: 350px;
	margin: 0;
}
</style>