game.resources = [
	/**
	 * Graphics.
	 */
	// our level tileset
	{name: "area01_level_tiles",  type:"image",	src:filepath+"data/img/map/area01_level_tiles.png"},
  {name: "x1intro",  type:"image",	src:filepath+"data/img/map/x1intro.png"},
	// the main player spritesheet
	{name: "gripe_run_right",     type:"image",	src: filepath+"data/img/sprite/gripe_run_right.png"},
  {name:"x_run_right", type:"image", src:filepath+"data/img/sprite/x_run_right.png"},
	// the parallax background
	{name: "area01_bkg0",         type:"image",	src: filepath+"data/img/area01_bkg0.png"},
	{name: "area01_bkg1",         type:"image",	src: filepath+"data/img/area01_bkg1.png"},
	
  // the spinning coin spritesheet
	{name: "spinning_coin_gold",  type:"image",	src: filepath+"data/img/sprite/spinning_coin_gold.png"},
	// our enemty entity
	{name: "wheelie_right",       type:"image",	src: filepath+"data/img/sprite/wheelie_right.png"},
	// game font
	{name: "32x32_font",          type:"image",	src: filepath+"data/img/font/32x32_font.png"},
	
	/* 
	 * Maps. 
 	 */
	{name: "area01",              type: "tmx",	src: filepath+"data/map/area01.tmx"},
  
	/* 
	 * Background music. 
	 */	
  {name:"x1intromusic",     type: "audio", src: filepath+"data/bgm/"},
	
	/* 
	 * Sound effects. 
	 */
];
