<template>
	<v-item-group multiple>
    <v-layout row class="pt-0 ma-0">
      <v-row class="category">
        <v-col
          v-for="(item, idx) in categoryItems"
          :key="idx"
          cols="4"
					class="items"
        >
          <v-item v-slot:default="{ active, toggle }">
            <v-card
              :color="active ? 'blue lighten-5' : 'white'"
              height="104px"
							flat
              @click="toggle"
							:class="active ? 'active-item-box' : 'item-box'"
            >
							<div @click="selectCategory(item.title)">
								<v-img :src="item.icon" class="store-icon"></v-img>
								<p class="mb-0">{{ item.title }}</p>
							</div>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
    </v-layout>
  </v-item-group>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
	data () {
		return {
			seleted: '',
			selectedCategory: [],
			categoryItems: [
				{ title: '한식', icon: 'https://image.flaticon.com/icons/svg/135/135669.svg'},
				{ title: '양식', icon: 'https://image.flaticon.com/icons/svg/135/135644.svg'},
				{ title: '아시아음식', icon: 'https://image.flaticon.com/icons/svg/135/135658.svg'},
				{ title: '일식', icon: 'https://image.flaticon.com/icons/svg/135/135659.svg'},
				{ title: '중식', icon: 'https://image.flaticon.com/icons/svg/135/135769.svg'},
				{ title: '분식', icon: 'https://image.flaticon.com/icons/svg/135/135599.svg'},
				{ title: '카페', icon: 'https://image.flaticon.com/icons/svg/135/135766.svg'},
				{ title: '뷔페', icon: 'https://image.flaticon.com/icons/svg/135/135607.svg'},
				{ title: '기타', icon: 'https://image.flaticon.com/icons/svg/135/135561.svg'},
				// '한식', '양식', '아시아음식', '일식', '중식', '분식', '카페', '뷔페', '기타'
			]
		}
	},
	created() {
		this.selected = false
	},
	methods: {
		...mapMutations('category', ['setCategory']),
		selectCategory (param) {
			this.setCategory(param)
		},
	}
}
</script>

<style scoped>
.category {
	margin: 0;
	padding: auto;
}
.category .items {
	height: 105px;
	border-top: 1px solid rgba(0, 0, 0, 0.1);
	border-right: 1px solid rgba(0, 0, 0, 0.1);
	padding: 0;
}
.active-item-box {
	color: #1976d2 !important;
	padding-top: 3vh;
	text-align: center;
}
.item-box {
	padding-top: 3vh;
	text-align: center;
}
.store-icon {
	width: 40px;
	margin: 0 auto;
}
</style>