

var Decode= function(){
	this.letters="acdegilmnoprstuw";
}

Decode.prototype.solve = function(hashValue){
	for(var i=0 ; i<this.letters.length ; ++i){
		if((hashValue-i)%37==0) {
			var hashtmp = (hashValue - i)/37;
			if(hashtmp < 37) {
				return this.letters[i];
			}
			else {
				return this.solve(hashtmp)+this.letters[i];
			}
		}
	}
}

var unHash= new Decode();
console.log( unHash.solve(680131659347) )


