<template>
  <q-layout view="hHh lpR fFr">
    <q-header reveal elevated class="bg-primary text-white">
      <NavBar>
        <q-btn
          round
          dense
          icon="bi-list"
          class="q-ml-lg"
          @click="rightDrawerOpen = !rightDrawerOpen" />
      </NavBar>
    </q-header>

    <!-- 作者信息 -->
    <q-drawer show-if-above v-model="rightDrawerOpen" side="right" bordered>
      <q-scroll-area class="fit">
        <!-- 名片 -->
        <q-card flat bordered class="q-mt-md q-ml-sm">
          <q-item>
            <q-item-section avatar>
              <q-avatar>
                <q-img :src="atcDetail.author?.avatar"></q-img>
              </q-avatar>
            </q-item-section>
            <q-item-section>
              <q-item-label class="text-subtitle1 text-weight-bold">
                {{ atcDetail.author?.username }}
              </q-item-label>
              <q-item-label>
                入住星球的第100天 <q-badge align="middle" color="grey">学富五车</q-badge>
              </q-item-label>
              <q-item-label caption> 累计发布10篇文章 </q-item-label>
            </q-item-section>
          </q-item>
          <q-card-actions class="q-px-md" align="right">
            <q-btn flat round color="red" icon="bi-person-plus">
              <q-tooltip transition-show="jump-down" transition-hide="jump-up"> 关注 </q-tooltip>
            </q-btn>
            <q-btn flat round color="accent" icon="bi-send">
              <q-tooltip transition-show="jump-down" transition-hide="jump-up"> 去主页 </q-tooltip>
            </q-btn>
          </q-card-actions>

          <q-separator />

          <q-card-section>
            <div class="q-px-lg q-pb-md">
              <q-timeline color="secondary">
                <q-timeline-entry heading tag="span" class="text-h6">时光轴</q-timeline-entry>

                <q-timeline-entry title="加入猿星球" subtitle="2023-1-1">
                  <div></div>
                </q-timeline-entry>

                <q-timeline-entry title="发布第一篇文章" subtitle="2023-1-3">
                  <div></div>
                </q-timeline-entry>

                <q-timeline-entry title="收获了第一个赞" subtitle="2023-1-9">
                  <div></div>
                </q-timeline-entry>
              </q-timeline>
            </div>
          </q-card-section>
        </q-card>
      </q-scroll-area>
    </q-drawer>

    <!-- 目录 -->
    <q-drawer v-model="leftDrawerOpen" side="left" bordered class="bg-grey-1">
      <q-card flat bordered class="q-ma-lg bg-blue-grey-1">
        <q-card-actions>
          <q-btn
            color="primary"
            label="返回上一页"
            outline
            dense
            icon="bi-arrow-left-short"
            @click="goBack" />
        </q-card-actions>
        <q-card-section>
          <div class="text-h5"><q-icon name="bi-list-ul"></q-icon> 目 录</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <div v-html="atcDetail.toc_html" id="toc"></div>
        </q-card-section>
      </q-card>
    </q-drawer>

    <!-- 文章 -->
    <q-page-container class="bg-grey-3">
      <q-scroll-area style="height: 85vh">
        <!-- 头部 -->
        <div class="q-pa-lg">
          <div class="text-h4 text-center">{{ atcDetail.title }}</div>
          <div class="text-caption text-right q-my-sm">
            <q-badge outline color="blue" class="q-mr-md">
              {{ atcDetail.category?.title }}
            </q-badge>
            <q-badge
              color="brown-6 "
              rounded
              class="q-mr-sm"
              v-for="tag in atcDetail.tags"
              :key="tag.index">
              {{ tag }}
            </q-badge>

            <q-icon name="bi-person-circle"></q-icon>
            {{ atcDetail.author?.username }}
            <q-icon name="bi-calendar3 q-ml-sm"></q-icon>
            {{ pubDate }}
          </div>
          <div class="q-mt-sm">
            <q-img :src="atcDetail.title_img?.img" :ratio="16 / 8"></q-img>
          </div>
        </div>

        <q-separator color="primary" inset />

        <!-- 正文 -->
        <div class="q-mx-lg">
          <div v-html="atcDetail.body_html"></div>
        </div>

        <q-separator color="primary" inset />

        <!-- 评论 -->
        <div class="q-pa-lg bg-grey-2">
          <div class="text-h5"><q-icon name="bi-chat-square-text" left></q-icon>评 论</div>
          <div class="q-mt-md">
            <q-card flat bordered class="bg-blue-grey-1">
              <!-- 未登录 -->
              <q-card-section v-if="!loginStore.isLogin">
                <div class="text-center q-pa-lg bg-blue-grey-2">
                  好像还没有登录
                  <q-btn
                    outline
                    color="primary"
                    dense
                    label="去登录"
                    @click="loginStore.isShowLogin = true" />
                </div>
              </q-card-section>

              <q-card-section v-if="loginStore.isLogin" class="q-pt-none">
                <div class="q-pa-md">
                  <q-input
                    v-model="commentText"
                    label="评论"
                    filled
                    type="textarea"
                    lazy-rules
                    :rules="[(val) => val.length > 0 || '请输入评论']" />
                  <div class="row justify-end">
                    <q-btn label="重置" color="primary" flat @click="commentText = ''" />
                    <q-btn label="提交" color="primary" />
                  </div>
                </div>
              </q-card-section>

              <!-- 全部评论 -->
              <q-card-section>
                <div class="text-h6">全部评论 {{ atcDetail.comments?.length }}</div>
              </q-card-section>
              <q-card-section>
                <div v-for="comment in atcDetail.comments" :key="comment.id">
                  <q-chat-message
                    :name="comment.author?.username"
                    :avatar="comment.author?.avatar"
                    :text="[comment.content]"
                    :stamp="new Date(comment.created).toLocaleString()"
                    text-color="white"
                    bg-color="blue-grey-6" />
                </div>
              </q-card-section>
            </q-card>
          </div>
        </div>
      </q-scroll-area>
      <!-- 回到顶部 -->
      <q-page-scroller position="bottom-right" :scroll-offset="150" :offset="[18, 18]">
        <q-btn fab icon="bi-chevron-compact-up" color="accent" />
      </q-page-scroller>
    </q-page-container>

    <!-- 底栏 -->
    <q-footer reveal class="bg-grey-3 text-black">
      <q-toolbar>
        <q-btn color="primary" round outline dense icon="bi-arrow-left-short" @click="goBack" />
        <q-space />
        <div class="q-gutter-x-lg">
          <q-btn flat round color="grey-8" icon="bi-hand-thumbs-up-fill" />
          <q-btn flat round color="grey-8" icon="bi-chat-square-text" />
          <q-btn flat round color="grey-8" icon="bi-share-fill" />
        </div>
        <q-space />
        <q-btn
          round
          outline
          dense
          icon="bi-list"
          color="primary"
          @click="rightDrawerOpen = !rightDrawerOpen" />
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { ref, onBeforeMount, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useLoginRegiStore } from 'stores/login-regi'
import { api } from 'boot/axios'
import NavBar from 'components/NavBar.vue'

let commentText = ref('')
const leftDrawerOpen = ref(true)
const rightDrawerOpen = ref(false)
const atcDetail = ref({})
const router = useRouter()
const loginStore = useLoginRegiStore()

const pubDate = computed(() => new Date(atcDetail.value.created).toLocaleString())

// 返回上一页
const goBack = () => {
  router.go(-1)
}

onBeforeMount(() => {
  const { id } = router.currentRoute.value.params
  api.get(`/article/${id}`).then((res) => {
    atcDetail.value = res.data
  })
})
</script>

<style scoped lang="scss"></style>
