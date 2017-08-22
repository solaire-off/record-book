var App = new Vue({
	delimiters: ["[", "]"],
	el : "#app",
	data : {
		students : [],
		marks : [],
		subjects : [],
		averageMarks : [],
	},
	created : function(){
		this.fetchData();
	},
	methods :{
		fetchData : function(){
			this.$http.get("/marks/?format=json")
				.then(response => {
					this.marks = response.data
				})
			this.$http.get("/students/?format=json")
				.then(response => {
					this.students = response.data
				})
			this.$http.get("/subjects/?format=json")
				.then(response =>{
					this.subjects = response.data
				})
			
		},
		shortName : function(student){
			return student.lastname+" "+ student.firstname[0]+ ". " + student.patronymic[0]+"."
		},
		findMarks : function(student,subject){
			return this.marks.results.filter(item =>{
					return item.student === student.url && item.subject === subject.url;
			})
		},
		averageMark : function(student){
			var sum = 0;
			var arr = this.marks.results.filter(item =>{
				return item.student === student.url;
			});
			var count = arr.length;
			arr.forEach(function(item) {
				sum += item.value; 
				});
			var result = (sum / count);
			if (!isNaN(result)){
				this.averageMarks.push(result);
				return result;
			}
			return "-"
		},
		groupMark : function(){
			var sum = 0;
			var arr = this.averageMarks;
			var count = arr.length;
			arr.forEach(function(item) {
				sum += item; 
				});
			var mark = sum / count; 
			return mark;
		}

	}
})

