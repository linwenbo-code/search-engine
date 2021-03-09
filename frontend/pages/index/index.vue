<template>
	<view class="">
		<u-form :model="form" ref="uForm">
			<u-form-item label="搜索" prop="query">
				<u-input v-model="form.query" />
			</u-form-item>
		</u-form>
		<u-button @click="submit">搜索</u-button>
		
		<!--
		<u-index-list :scrollTop="scrollTop">
			<view v-for="item in resultList" :key="index">
				<u-index-anchor :index="item['信息提供方']" />
				<view class="list-cell">
					{{ JSON.stringify(item) }}
				</view>
			</view>
		</u-index-list>
		-->
		
		<ol>
			<u-divider color="#fa3534">共搜索到 {{ resultList.length }} 条记录</u-divider>
			<li v-for="(item, index) in resultList">
				<u-divider color="#fa3534">第 {{ index+1 }} 条记录</u-divider>
				{{ JSON.stringify(item) }}
			</li>
		</ol>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				form: {
					query: ''
				},
				rules: {
					query: [
						{ 
							required: true, 
							message: '请输入搜索内容', 
							// 可以单个或者同时写两个触发验证方式 
							trigger: ['change','blur'],
						}
					]
				},
				scrollTop: 0,
				resultList: []
			}
		},
		onPageScroll(e) {
			this.scrollTop = e.scrollTop;
		},
		onLoad() {
			
		},
		methods: {
			submit() {
				this.$refs.uForm.validate(valid => {
					if (valid) {
						console.log('验证通过');
					} else {
						console.log('验证失败');
					}
					console.log('搜索内容：' + this.form.query)
					uni.request({
					    url: 'http://localhost:8888', 
						method: 'POST',
						/*
						header: {
							'Content-Type': 'application/json'
						},
						*/
					    data: this.form.query,
					    success: (res) => {
					        console.log(res.data);
							console.log('round trip completed. ')
							console.log('type of ' + typeof(JSON.stringify(res.data)))
							console.log(JSON.stringify(res.data))
							this.resultList = res.data;
						},
						fail: function(res) {
							console.log(res);
						}
					});
				});
			}
		},
		// 必须要在onReady生命周期，因为onLoad生命周期组件可能尚未创建完毕
		onReady() {
			this.$refs.uForm.setRules(this.rules);
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
	
	.list-cell {
		display: flex;
		box-sizing: border-box;
		width: 100%;
		padding: 10px 24rpx;
		overflow: hidden;
		color: #323233;
		font-size: 14px;
		line-height: 24px;
		background-color: #fff;
	}
</style>
