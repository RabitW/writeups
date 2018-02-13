var level = 0x46;
var rect_w = 0x2d;
var rect_h = 0x1e;
var inc_score = 0x32;
var snake_color = '#006699';
var ctx;
var tn = [];
var x_dir = [-0x1, 0x0, 0x1, 0x0];
var y_dir = [0x0, -0x1, 0x0, 0x1];
var queue = [];
var frog = 0x1;
var map = [];
var MR = Math['random'];
var X = 0x5 + MR() * (rect_w - 0xa) | 0x0;
var Y = 0x5 + MR() * (rect_h - 0xa) | 0x0;
var direction = MR() * 0x3 | 0x0;
var interval = 0x0;
var score = 0x0;
var sum = 0x0,
	easy = 0x0;
var i, dir;
var c = document['getElementById']('playArea');
ctx = c['getContext']('2d');
for (i = 0x0; i < rect_w; i++) map[i] = [];

function rand_frog() {
	var _0x286ac2, _0x2a3620;
	do {
		_0x286ac2 = MR() * rect_w | 0x0;
		_0x2a3620 = MR() * rect_h | 0x0;
	} while (map[_0x286ac2][_0x2a3620]);
	map[_0x286ac2][_0x2a3620] = 0x1;
	ctx['fillStyle'] = snake_color;
	ctx['strokeRect'](_0x286ac2 * 0xa + 0x1, _0x2a3620 * 0xa + 0x1, 0x8, 0x8);
}
rand_frog();

function set_game_speed() {
	if (easy) {
		X = (X + rect_w) % rect_w;
		Y = (Y + rect_h) % rect_h;
	}--inc_score;
	if (tn['length']) {
		dir = tn['pop']();
		if (dir % 0x2 !== direction % 0x2) {
			direction = dir;
		}
	}
	if ((easy || 0x0 <= X && 0x0 <= Y && X < rect_w && Y < rect_h) && 0x2 !== map[X][Y]) {
		if (0x1 === map[X][Y]) {
			score += Math['max'](0x5, inc_score);
			inc_score = 0x32;
			rand_frog();
			frog++;
		}
		ctx['fillRect'](X * 0xa, Y * 0xa, 0x9, 0x9);
		map[X][Y] = 0x2;
		queue['unshift']([X, Y]);
		X += x_dir[direction];
		Y += y_dir[direction];
		if (frog < queue['length']) {
			dir = queue['pop']();
			map[dir[0x0]][dir[0x1]] = 0x0;
			ctx['clearRect'](dir[0x0] * 0xa, dir[0x1] * 0xa, 0xa, 0xa);
		}
	} else if (!tn['length']) {
		var _0x1e212d = document['getElementById']('msg');
		_0x1e212d['innerHTML'] = 'Thank\x20you\x20for\x20playing\x20game.<br\x20/>\x20Your\x20Score\x20:\x20<b>' + score + '</b><br\x20/><br\x20/><input\x20type=\x27button\x27\x20value=\x27Play\x20Again\x27\x20onclick=\x27window.location.reload();\x27\x20/>';
		if (score > 0x186a0) {
			_0x1e212d['innerHTML'] = 'Thank\x20you\x20for\x20playing\x20game.<br\x20/>\x20Your\x20Score\x20:\x20<b>' + score + '</b><br\x20/>' + String['fromCharCode'](0x46, 0x4c, 0x41, 0x47, 0x7b, 0x79, 0x30, 0x75, 0x5f, 0x72, 0x65, 0x5f, 0x70, 0x72, 0x30, 0x67, 0x61, 0x6d, 0x33, 0x72, 0x7d) + '<br\x20/><input\x20type=\x27button\x27\x20value=\x27Play\x20Again\x27\x20onclick=\x27window.location.reload();\x27\x20/>';
		} else document['getElementById']('playArea')['style']['display'] = 'none';
		window['clearInterval'](interval);
	}
	document['getElementById']('score')['innerHTML'] = 'Score:\x20' + score;
}
interval = window['setInterval'](set_game_speed, level);
document['onkeydown'] = function(_0x263f79) {
	var _0x1688bc = _0x263f79['keyCode'] - 0x25;
	if (0x0 <= _0x1688bc && _0x1688bc < 0x4 && _0x1688bc !== tn[0x0]) {
		tn['unshift'](_0x1688bc);
	} else if (-0x5 == _0x1688bc) {
		if (interval) {
			window['clearInterval'](interval);
			interval = 0x0;
		} else {
			interval = window['setInterval'](set_game_speed, 0x3c);
		}
	} else {
		dir = sum + _0x1688bc;
		if (dir == 0x2c || dir == 0x5e || dir == 0x7e || dir == 0xab) {
			sum += _0x1688bc;
		} else if (dir === 0xda) easy = 0x1;
	}
};