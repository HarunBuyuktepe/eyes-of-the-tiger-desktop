<template>
	<v-container fluid fill-height style="background: #F3E7E5">
		<img
			src="../../assets/White-Tiger-Face-HD-1920x1080.jpg"
			style="position: fixed; "
		/>
		<vue-core-video-player
			:src="require('./Demo.mp4')"
			style="height: 500px; width:920px; left: 35px "
		></vue-core-video-player>
	</v-container>
</template>

<script>
	export default {
		name: "AboutUs",
		created() {
			console.log("aboju")
		},
		data() {
			return {
				cicek: "./deno.mp4"
			};
		},
	};
</script>
