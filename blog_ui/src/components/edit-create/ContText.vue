<template>
  <q-card class="bg-blue-grey-1">
    <q-card-section>
      <div class="text-h5 text-center">{{ pageTitle }}</div>
      <div class="text-subtitle2 text-right">by username</div>
    </q-card-section>

    <q-separator />

    <q-card-section>
      <div class="q-pa-md">
        <div class="q-gutter-md">
          <q-input
            filled
            v-model="articleInfo.title"
            label="文章标题"
            lazy-rules
            :rules="[(val) => !!val || '请输入文章标题']">
            <template v-slot:prepend>
              <q-icon name="bi-type-h1"></q-icon>
            </template>
          </q-input>

          <div class="row">
            <div class="col-6 q-pr-sm">
              <q-file filled bottom-slots v-model="articleInfo.title_img" label="文章标题图片">
                <template v-slot:prepend>
                  <q-icon name="bi-cloud-arrow-up-fill" @click.stop />
                </template>
                <template v-slot:append>
                  <q-icon
                    name="bi-x"
                    @click.stop="articleInfo.title_img = null"
                    class="cursor-pointer" />
                </template>
                <template v-slot:hint> 非必填项 </template>
              </q-file>
            </div>
            <div class="col-6 q-pl-sm">
              <q-select
                filled
                v-model="articleInfo.category"
                :options="cgList"
                option-value="id"
                option-label="title"
                emit-value
                map-options>
                <template v-slot:prepend>
                  <q-icon name="bi-ui-checks-grid" />
                </template>
                <template v-slot:append>
                  <q-icon
                    v-if="articleInfo.category"
                    name="bi-x"
                    @click.stop="articleInfo.category = ''"
                    class="cursor-pointer" />
                </template>
              </q-select>
            </div>
          </div>

          <q-input
            dense
            filled
            v-model.trim="tagText"
            label="自定义文章标签"
            hint="输入标签名称后按下Enter键完成添加"
            @keyup.enter="addTag">
            <template v-slot:prepend>
              <q-icon name="bi-bookmark-plus-fill" />
            </template>
          </q-input>
          <div class="q-mx-lg" v-if="articleInfo.tags.length">
            标签：
            <q-chip
              outline
              color="pink-12"
              text-color="white"
              v-for="tg in articleInfo.tags"
              :key="tg.index">
              {{ tg }}
              <q-btn
                flat
                dense
                round
                icon="bi-x"
                size="sm"
                right
                @click="articleInfo.tags = articleInfo.tags.filter((item) => item !== tg)" />
            </q-chip>
          </div>

          <!-- 编辑器 -->
          <div class="q-mt-lg text-subtitle1">
            <q-icon name="bi-pencil-square"></q-icon> 文本编辑
          </div>
          <div class="q-mt-none">
            <q-bar class="bg-blue-grey-2 text-black">
              <q-btn flat dense round icon="bi-type-bold" @click="editToolbar.boldFn" />
              <q-btn flat dense round icon="bi-type-italic" @click="editToolbar.italicFn" />
              <q-btn flat dense round icon="bi-type-strikethrough" @click="editToolbar.delFn" />
              <q-btn flat dense round icon="bi-type-underline" @click="editToolbar.underlineFn" />
              <q-btn flat dense round icon="bi-link" @click="editToolbar.linkFn" />
              <q-btn flat dense round icon="bi-code" @click="editToolbar.codeRowFn" />
              <q-btn flat dense round icon="bi-code-slash" @click="editToolbar.codeBlockFn" />
              <!-- <q-space /> -->
            </q-bar>
            <q-input
              id="md-editor"
              v-model="articleInfo.mdCont"
              outlined
              type="textarea"
              hint="目前仅支持Markdown语法，文本内容大于100字可提交"
              lazy-rules
              :rules="[(val) => val.length > 1 || '文本内容过短']" />
          </div>
        </div>
      </div>
    </q-card-section>

    <q-separator />

    <q-card-actions align="right" class="q-pa-lg">
      <q-btn color="positive" size="sm" icon="bi-send" :label="pageTitle" @click="publishArticle" />
      <q-btn
        color="blue-grey-6"
        size="sm"
        icon="bi-backspace-fill"
        label="退出编辑"
        @click="exitEdit" />
    </q-card-actions>
  </q-card>
</template>

<script setup>
import { api } from "boot/axios"
import { nfy } from "src/utils/u-notify.js"
import { loginAuth, useLoginRegiStore } from "stores/login-regi"
import { computed, onBeforeMount, reactive, ref, watch } from "vue"
import { useRoute, useRouter } from "vue-router"

let articleInfo = reactive({
  title: "",
  mdCont: "",
  title_img: null,
  title_img_id: null,
  tags: [],
  category: null,
})
let tagText = ref("")
const cgList = ref([])
const route = useRoute()
const router = useRouter()
const loginStore = useLoginRegiStore()
const editToolbar = {
  boldFn: () => {
    articleInfo.mdCont += "****"
  },
  italicFn: () => {
    articleInfo.mdCont += "**"
  },
  delFn: () => {
    articleInfo.mdCont += "~~"
  },
  underlineFn: () => {
    articleInfo.mdCont += "__"
  },
  linkFn: () => {
    articleInfo.mdCont += "[]()"
  },
  codeRowFn: () => {
    articleInfo.mdCont += "``"
  },
  codeBlockFn: () => {
    articleInfo.mdCont += "```\n```"
  },
}

const pageTitle = computed(() => {
  return route.path === "/edit" || route.params.id === "" ? "发布文章" : "更新文章"
})

const addTag = () => {
  if (tagText.value) {
    if (!articleInfo.tags.includes(tagText.value)) {
      articleInfo.tags.push(tagText.value)
      tagText.value = ""
    } else {
      tagText.value = ""
      nfy("warning", "标签已存在", 1000, "center")
    }
  }
}

// 退出编辑
const exitEdit = () => {
  if (
    articleInfo.title ||
    articleInfo.mdCont ||
    articleInfo.title_img ||
    articleInfo.tags.length ||
    articleInfo.category
  ) {
    if (confirm("文章有更新，是否退出编辑？")) {
      router.push({ name: "ArticleList" })
    }
  } else {
    router.push({ name: "ArticleList" })
  }
}

// 验证必要字段
const isImportenceValid = () => {
  if (articleInfo.title && articleInfo.mdCont) {
    return true
  } else {
    nfy("warning", "请填写文章标题和内容", 1000, "center")
    return false
  }
}

watch(
  () => articleInfo.title_img,
  (val) => {
    if (val) {
      let formData = new FormData()
      formData.append("img", val)
      api({
        method: "post",
        url: "titleimg/",
        data: formData,
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: "Bearer " + localStorage.getItem("pa.token"),
        },
      }).then((res) => {
        articleInfo.title_img_id = res.data.id
      })
    }
  }
)

const createArticle = () => {
  api
    .post(
      "article/",
      {
        title: articleInfo.title,
        md_cont: articleInfo.mdCont,
        title_img_id: articleInfo.title_img_id,
        tags: articleInfo.tags,
        category_id: articleInfo.category,
      },
      {
        headers: {
          Authorization: "Bearer " + localStorage.getItem("pa.token"),
        },
      }
    )
    .then((res) => {
      nfy("positive", "发布成功", 1000, "center")
      router.push({ name: "ArticleDetail", params: { id: res.data.id } })
    })
    .catch((err) => {
      nfy("negative", `文章发布失败~${err.message}`, 1000, "center")
    })
}

const updateArticle = () => {}

const publishArticle = () => {
  if (isImportenceValid()) {
    // 登录是否过期
    loginAuth().then((resp) => {
      if (resp) {
        // 发布文章
        if (route.path === "/edit" || route.query.id === "") {
          createArticle()
        } else {
          updateArticle()
        }
      } else {
        nfy("negative", "登录已过期，请重新登录", 1000, "center")
        loginStore.isShowLogin = true
      }
    })
  }
}

onBeforeMount(async () => {
  const { data } = await api.get("category/")
  cgList.value = data
})
</script>
