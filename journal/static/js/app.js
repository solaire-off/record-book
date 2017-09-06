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
			this.$http.get("/students/?format=json")
				.then(response => {
					this.students = response.data
				})
			this.$http.get("/subjects/?format=json")
				.then(response =>{
					this.subjects = response.data;
					this.fetchMarks();
					
				})
		},
		fetchMarks: function(){
			var self = this;
			self.students.results.forEach(function(student) {
				self.subjects.results.forEach(function(subject) {
					var url = "/marks/?student="+student.id+"&subject="+subject.id;
					self.$http.get(url)
						.then(function(response)  {
							if (response.data.count){
								var key = student.id+'_'+subject.id;
								var data = response.data.results;
								self.marks.push({
									key: key ,
									value: data
									});
								
							}											
						});
					});
				});
			
		},
		shortName : function(student){
			return student.lastname+" "+ student.firstname[0]+ ". " + student.patronymic[0]+"."
		},
		getMarks : function(student,subject){
			var key = student.id+'_'+subject.id;
			var search = this.marks.filter(function( obj ) {
  				return obj.key == key;
			});
			var result = [];
			search.forEach(function(object) {
				result.push(object.value)
			});
			return result[0];		
		}
	},
})

