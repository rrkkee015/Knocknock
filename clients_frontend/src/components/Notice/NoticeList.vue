<template>
	<v-container>
		<p class="font-headline">공지사항</p>
		<v-list>
      <v-list-group 
				v-for="(notice, idx) in notices"
				:key="idx"
				no-action
				class="list-group-border"
			>
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title style="overflow: visible; white-space: inherit;">
							{{ notice.title }}
						</v-list-item-title>
          </v-list-item-content>
        </template>
        <v-list-item class="pl-6">
          <v-list-item-content>
						{{ notice.content }}
          </v-list-item-content>
        </v-list-item>
      </v-list-group>
    </v-list>
	</v-container>
</template>

<script>
import { mapState } from 'vuex'
export default {
	computed: {
		...mapState('notice', ['notices'])
	}
}
</script>

<style scoped>
.font-headline {
  font-size: 24px;
  font-weight: 700;
}
.list-group-border {
	border-bottom: 0.5px solid rgba(0, 0, 0, 0.3);
}
</style>