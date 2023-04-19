import { defineStore } from "pinia"

export const useSearchUrlStore = defineStore("SearchUrl", {
  state: () => ({
    baseUrl: "article/",

    // 搜索字段
    searchTitle: "",
    category: "",
    created: "",
    tabName: "defu",

    // 分页
    pageNum: 1,
  }),

  getters: {
    getUrl: (state) => {
      let tmpUrl = "article/"
      if (state.searchTitle || state.category || state.created) {
        tmpUrl += `?title=${state.searchTitle}&category=${state.category}&created=${state.created}`
        console.log(tmpUrl)
        return tmpUrl
      }
      if (state.pageNum > 1) {
        tmpUrl += `?page=${state.pageNum}`
        return tmpUrl
      }
      return state.baseUrl
    },
  },

  actions: {
    // 搜索事件
    setSearch(searchKey) {
      this.searchTitle = searchKey
    },

    // 分页事件
    setPageNum(pageNum) {
      this.pageNum = pageNum
    },

    setTabName(tabName) {
      this.tabName = tabName
      if (tabName === "latest") {
        this.created = "latest"
      } else {
        this.created = ""
      }
    },
  },
})
