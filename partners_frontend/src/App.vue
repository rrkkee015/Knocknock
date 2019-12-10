<template>
  <v-app>
    <Header
      v-if="headerToggle"
    />
    <Nav/>
    <router-view/>
  </v-app>
</template>

<script>
import Header from '@/components/common/Header'
import Nav from '@/components/common/NavigationDrawer'
import { mapState } from 'vuex'

export default {
  name: 'App',
  components: {
    Header,
    Nav
  },
  data: () => ({
    //
  }),
  computed: {
    ...mapState('drawer', ['headerToggle'])
  }
}
</script>

<style scoped>

</style>
