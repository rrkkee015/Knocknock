const state = {
	selectedCategory: []
}

const mutations = {
	setCategory (state, param) {
		if (param === 'init') {
			state.selectedCategory =[]
		} else {
			if (!state.selectedCategory.includes(param)) {
				state.selectedCategory.push(param)
			} else {
				state.selectedCategory.splice(state.selectedCategory.indexOf(param), 1)
			}
		}
	}
}

export default {
	namespaced: true,
	state,
	mutations
  }