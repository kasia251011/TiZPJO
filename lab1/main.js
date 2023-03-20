#!/usr/bin/env node
process.stdin.resume();
process.stdin.setEncoding('utf8');

var lingeringLine = "";

function my_printf(format_string,param){
	for(var i=0;i<format_string.length;i++){
		if((format_string.charAt(i) == '#') && (format_string.charAt(i+1) == 'k')){
			
			param = toggleLetterCase(param);

			process.stdout.write(param);
			i++;
		}else{
			process.stdout.write(format_string.charAt(i));
		}
	}
	console.log("");
}

function toggleLetterCase (param) {
	for(let i = 0; i < param.length; i++) {
		
		const letter = param[i];

		if (letter == letter.toUpperCase()) {
			param.replaceAt(i, letter.toLowerCase());
		} else {
			param.replaceAt(i, letter.toUpperCase());
		}
	}

	return param;
}

String.prototype.replaceAt = function(index, replacement) {
	return this.substring(0, index) + replacement + this.substring(index + replacement.length);
}

process.stdin.on('data', function(chunk) {
	lines = chunk.split("\n");

	lines[0] = lingeringLine + lines[0];
	lingeringLine = lines.pop();
	for(var i=0;i<lines.length;i++){
		my_printf(lines[i],lines[i+1])
		i++;
	}

});

