# Create your views here.

from django.shortcuts import render_to_response
from openlpwebapp.songs.models import Song
from openlpwebapp.songs.forms import SongSearchForm
from xml.dom.minidom import parseString
from django.template.context import RequestContext

def search_songs(request):
    form = SongSearchForm(request.GET)
    
    if(form.is_valid()):
        formData = form.cleaned_data
        songs = Song.objects.filter(title__icontains=formData['title'])
        print "Request path", request.path
        print "Request url", request.environ.get('PATH_INFO')
        return render_to_response('search_songs.html', {'songs':songs, 'form':form, 'query':formData['title']}, 
                                  context_instance=RequestContext(request))
    else:
        form = SongSearchForm()
        return render_to_response('search_songs.html', {'form':form})
    
def song_lyrics(request, song_id):
    songs = Song.objects.filter(id=song_id)      
    song = songs[0]      
    formattedLyrics = getFormattedLyrics(song.lyrics)
    formattedLyrics = formattedLyrics.replace("\n", "<br>")
    return render_to_response('song_lyrics.html', {'song':song, 'verses':formattedLyrics.split("\r")})

def getFormattedLyrics(lyricsXml):    
    dom = parseString(lyricsXml)
    verses = dom.getElementsByTagName("verse")
    return getText(verses)    

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
        else:
            rc.append(node.firstChild.wholeText)
            rc.append("\r")            
    return ''.join(rc)
