<template>
<div class="px-5 py-5">
	<div v-if="menus.length">
		<v-row
			v-for="(menu, idx) in menus"
			:key="idx"
		>
			<v-col 
				cols="8"
				class="menu-name"
			>	
			<v-tooltip 
				bottom
				max-width="350px"
			>
				<template v-slot:activator="{ on }">
					<span v-on="on">{{ menu.name }}</span>
				</template>
				<span>{{ menu.name }}</span>
				<v-img 
					v-if="menu.thumbnail"
					:src="menu.thumbnail"
					class="menu-thumbnail"
				>

				</v-img>
			</v-tooltip>
				<!-- {{ menu.name }} -->
			</v-col>
			<v-col 
				cols="4"
				class="menu-price"
			>	
				{{ menu.price }}원
			</v-col>
			<v-col 
				v-if="idx != menus.length -1"
				cols="12"
				class="menu-divider"
			>
				<v-divider></v-divider>
			</v-col>
		</v-row>
	</div>
	<div v-else>
		<p class="none-content">등록된 메뉴가 없어요.</p>
	</div>
</div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
	computed: {
		...mapGetters('store', ['menus'])
	}
}
</script>

<style scoped>
.menu-name {
	display: block;
	font-size: 15px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
	padding: 4px 12px;
}
.menu-price {
	text-align: right;
	font-size: 15px;
	padding: 4px 12px;
}
.menu-divider {
	padding: 4px 12px;
}
.none-content {
	font-size: 14px;
	color: grey;
}
.menu-thumbnail {
	height: 300px;
	object-fit: none;
	margin: 12px 0;
}
</style>