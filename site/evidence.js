'use strict';
(()=>{
 const $=id=>document.getElementById(id),size=12;
 let catalog=[],doc=null,items=[],page=0,blobURL=null;
 const hex=bytes=>Array.from(new Uint8Array(bytes),x=>x.toString(16).padStart(2,'0')).join('');
 function render(){
  const query=$('evidenceSearch').value.trim().replace(/^#/,'').toLowerCase();
  const filtered=items.filter(x=>!query||(/^\d+$/.test(query)?String(x.pr??x.number??'')===query:JSON.stringify(x).toLowerCase().includes(query)));
  page=Math.min(page,Math.max(0,Math.ceil(filtered.length/size)-1));
  const chosen=filtered.slice(page*size,(page+1)*size);
  const header={schema:doc.schema,scope:doc.scope,summary:doc.summary,total_matching_entries:filtered.length};
  $('evidenceContent').textContent=JSON.stringify(items.length?{...header,entries:chosen}:doc,null,2).slice(0,250000);
  $('pageStatus').textContent=items.length?`${filtered.length.toLocaleString()} matching entries · page ${page+1} of ${Math.max(1,Math.ceil(filtered.length/size))}`:'Complete JSON document';
  $('previousPage').disabled=page===0;$('nextPage').disabled=(page+1)*size>=filtered.length;
 }
 async function load(){
  const selected=catalog.find(x=>x.id===$('ledgerSelect').value);if(!selected)return;
  $('evidenceStatus').className='status';$('evidenceStatus').textContent='Loading and verifying original JSON…';
  try{
   const response=await fetch('data/'+selected.file);if(!response.ok)throw Error('Evidence download failed.');
   let bytes=new Uint8Array(await response.arrayBuffer());
   if(bytes[0]===31&&bytes[1]===139)bytes=new Uint8Array(await new Response(new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'))).arrayBuffer());
   const digest=hex(await crypto.subtle.digest('SHA-256',bytes));
   if(digest!==selected.original_sha256||bytes.length!==selected.original_bytes)throw Error('The evidence differs from its pinned original bytes.');
   doc=JSON.parse(new TextDecoder().decode(bytes));
   const candidate=Array.isArray(doc)?doc:(doc.rows??doc.entries??doc.files??doc.candidates??[]);items=Array.isArray(candidate)?candidate:[];page=0;
   $('evidenceStatus').textContent=`SHA-256 verified · ${bytes.length.toLocaleString()} original bytes${items.length?' · '+items.length.toLocaleString()+' entries':''}`;
   if(blobURL)URL.revokeObjectURL(blobURL);blobURL=URL.createObjectURL(new Blob([bytes],{type:'application/json'}));
   $('originalDownload').href=blobURL;$('originalDownload').download=selected.original_file.split('/').pop();$('originalDownload').hidden=false;
   $('compressedDownload').href='data/'+selected.file;$('compressedDownload').download=selected.original_file.split('/').pop()+'.gz';$('compressedDownload').hidden=false;
   history.replaceState(null,'','?file='+encodeURIComponent(selected.id));render();
  }catch(error){$('evidenceStatus').className='status error';$('evidenceStatus').textContent=error.message;}
 }
 $('ledgerSelect').addEventListener('change',load);
 $('evidenceSearch').addEventListener('input',()=>{page=0;if(doc)render();});
 $('previousPage').addEventListener('click',()=>{page--;render();});$('nextPage').addEventListener('click',()=>{page++;render();});
 fetch('data/compressed-evidence-catalog.json').then(r=>{if(!r.ok)throw Error('Evidence index unavailable.');return r.json();}).then(data=>{
  catalog=data.files;for(const entry of catalog){const option=document.createElement('option');option.value=entry.id;option.textContent=entry.label;$('ledgerSelect').append(option);}
  const query=new URLSearchParams(location.search),requested=query.get('file');if(catalog.some(x=>x.id===requested))$('ledgerSelect').value=requested;if(query.get('pr'))$('evidenceSearch').value=query.get('pr');return load();
 }).catch(error=>{$('evidenceStatus').className='status error';$('evidenceStatus').textContent=error.message;});
})();
