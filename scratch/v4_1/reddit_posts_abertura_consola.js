// Correr na consola do Chrome (F12 > Console) com um separador aberto em https://www.reddit.com
// Lê só o post de abertura de 59 tópicos e descarrega o ficheiro reddit_posts_abertura.json
(async () => {
  const ids = ['1eoyf2u', '1gebstj', '1hlv8xy', '1i6m4i6', '1jukb0x', '1kh1a1v', '1mctiz6', '1mwoeow', '1ofu78l', '1oq9poa', '1ph9o3i', '1rmfr5h', '1s9et4k', '1sv241g', '1t01k13', '1t3g4bt', '1tdxixs', '1tkscsd', '1twaq1l', '1tyovbz', '1udu43k', '1upzjbr', '1uqtdhy', '1v18nfp', '1vt5t85', '1w4y0sn', '1waqgod', '11kumll', '1ariy3g', '1d8nm29', '1kylpvy', '1nvtk44', '1ormrc6', '1p38i14', '1pftbpi', '1phwb0r', '1q7m0sl', '1ql5f05', '1r1dd9i', '1r3mzvw', '1r77r09', '1r77s3x', '1rg6iqz', '1rhkho1', '1rnbqbh', '1rq35g3', '1s5tj3u', '1sf61mq', '1snmfut', '1spdcd4', '1sq7b1r', '1t939or', '1tdr4z8', '1tvlpnw', '1u0bxq6', '1usj0hv', '1v3v2p2', '1vdomcq', '1vy3jwo'];
  const out = {};
  for (const id of ids) {
    try {
      const r = await fetch(`https://www.reddit.com/comments/${id}/.json?limit=1&raw_json=1`);
      const d = (await r.json())[0].data.children[0].data;
      out[id] = {id, title: d.title, selftext: d.selftext, author: d.author, created_utc: d.created_utc,
                 subreddit: d.subreddit, url: d.url, is_self: d.is_self, num_comments: d.num_comments};
    } catch (e) { out[id] = {id, erro: String(e)}; }
    console.log(Object.keys(out).length + "/" + ids.length, id);
    await new Promise(s => setTimeout(s, 1500));
  }
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([JSON.stringify(out, null, 1)], {type: "application/json"}));
  a.download = "reddit_posts_abertura.json";
  a.click();
})();
