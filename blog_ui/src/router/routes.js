const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("layouts/ArticleLayout.vue"),
    children: [{ path: "", name: "ArticleList", component: () => import("pages/ArticleList.vue") }],
  },
  {
    path: "/article/:id(\\d+)",
    name: "ArticleDetail",
    component: () => import("pages/ArticleDetail.vue"),
  },
  {
    path: "/edit/:id(\\d+)?",
    name: "EditCreate",
    component: () => import("pages/EditCreate.vue"),
    meta: { reqAuth: true },
  },
  {
    path: "/news",
    name: "News",
    component: () => import("pages/NewsPage.vue"),
  },
  {
    path: "/about",
    name: "About",
    component: () => import("pages/AboutPage.vue"),
  },
  {
    path: "/help",
    name: "Help",
    component: () => import("pages/HelpPage.vue"),
  },
  {
    path: "/:catchAll(.*)*",
    name: "NotFound",
    component: () => import("pages/ErrorNotFound.vue"),
  },
]

export default routes
