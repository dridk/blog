//===========================================================================
function encode(txt){
var code = ['A','C','G','T'];
var output = "";
	for (var i in txt)
	{
	var raw = txt[i].charCodeAt(0).toString(4);
	acgt = raw.replace(/0|1|2|3/g, function lambda(x){return code[x];});
	output+=acgt;
  }
return output;
}
//===========================================================================
function decode(txt){
var code = {'A':0,'C':1,'G':2,'T':3};
var output = "";
	for (var i=0; i<txt.length; i+=4)
	{
	acgt  = txt.substring(i,i+4);
	bases = acgt.replace(/A|C|G|T/g, function lambda(x){return code[x];});
  output+=String.fromCharCode(parseInt(bases,4));

	}

	return output;

}

console.log(decode("CATACGACCCTTCGATCGTTCTCCCTAGCGAGCGCC"))
