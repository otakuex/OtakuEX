# OtakuEX
Otaku Explorer - A guided exploration of the Anime World with your known likes and interests as a compass.

__Thesis of a Cool Angle:__

In the last 15 years or so, anime titles have exploaded in numbers due to advances in technology making the production process [easier/faster/better/cheaper](https://www.youtube.com/watch?v=GDpmVUEjagg&t=1m53s). This is a double-edged sword. While there's more to choose from, there's also more titles that you subjectively don't care for and more objectively bad titles that should've never been made in the first place. Wading through these can be tiring for the most enthusiastic anime fan. That's where we come in - start with the page for any title you like and explore out from there. Maybe you only care about the visuals of a show, or only want certain story types or themes. No problem! Our similarities rating system will help you find your personal diamonds in the rough.

__Purpose of this project:__
- Scrape information about anime series/movies from [Wikipedia](https://en.wikipedia.org/wiki/List_of_anime_companies/), [AniDB.net](http://anidb.net/) (may be a TOS conflict), and other sources to build a DB of all info available and display it in a front end web UI.
- Expand beyond Anime to include Manga, films, live action series, video games, books, etc.
- Allow and encourage user ratings on quality and similarity of different titles based on multiple categories (i.e. "this show is like this other in terms of visual style, but more like this other-other one in terms of story and themes").
- Once there is a well developed rating of similarities, users can see titles of interest from other users of similar likes or demographic profiles.

__Additional goals that may be outside this project:__
- Front page news feed with topics relavent to the Anime Community, like [AnimeNewsNetwork](https://www.animenewsnetwork.com), but smarter with custom feed categories targeting individual user interests, like [Google News](https://news.google.com/).
- Community forums with auto-promotion of users to mods and admins. Once certain levels are reached, users can elect to complete a site standards and practices course to be allowed to post articles to the front page news stream with content and tone appropriate to the site. These posts will be subject to peer review before going public.
- Other unidentified benefits to the community (e.g. Gaming voice chat service, list of trusted retailers by region, cosplay general tutorials and discussion like [The PropTarts of Punished Props](https://www.facebook.com/groups/theproptarts/), cosplay photo galleries separated by media type like anime/manga, video game, comic book, etc.).

__Component/Feature Build Order:__
- Scraper to build local database of anime titles and their respective production companies, staff, cast, etc. Source would be Wikipedia. Scraper must be reliable enough to run daily.
- Build handling process for new items and changes to existing items found by the scraper. Acceptable to make a widard-like process to have end users manually sort/approve changes and additions where 
- Build additional scraper(s) to pull info from other source(s) such as AniDB.net, MyAnimeList.net, and others where respective ToS' allow.
- Build basic web UI to display confirmed database listings.

>The above I can do; database with a main table of titles and a second of titles that may be the same or unique and waiting for users to decide if they should be merged or becone new titles in the main table. After this point I don't know how to structure the database or even what kind of database to use.

- Build feature for web UI that prompts users to rate and sort titles:
	- Rate how well they know the displayed title.
	- Pick several titles from a list that they are also familar with.
	- Rate the similarities of each title on a different-to-same scale fro multiple components (music, visual style, themes, etc.)
	- Ask user if they want to rate more titles.
	- Give user point for participating and increase over time with more interaction and dependant on answers being similar to other users'. The participation combined with answer similarity scores will combine into the user's confidence score.
	- Record the provided answers along with user ID and stated familarity level. The familarity level will be weighted against the user's confidence score. The result, combined with those of other users', will be what determines the final ratings of similarities between the components of titles, and thus of the titles themselves.
	- Answers should be stored in such a way that it can be sorted to only show only answers from users in the same region, or other user bio criteria, or that speak the same language, or that prefer subs over dubs (i.e. People that like Japanses DragonBall and not the same as people who like Funimation's DragonBall), etc.

>I can't have a title record in a table store info like "this user with this confidence score (changes over time) said this title's music is 70% similar to this other title's music" and then "another user said these other things". Maybe I could make that all it's own table with links to other tables? But some of the info needs to be calculated in real time based on multiple live factors. IDK.
	
- Update the basic web UI to include suggestions of overall similar titles and of titles with strongly similar individual components.
	- Provide display options for results from users with similar liked titles, similar bios, same region, specify different region, etc.
- Build 2D "Anime World" map where titles are plotted vertically by their maturity level (childish at South Pole, general audience titels along the equator, and mature/intellectual titles at North Pole) and horizontally by their genre (Shonen/action in Eastern Hemisphere, shoujo/romance in the Western hemisphere.
	- Other genres like slice of life, comedy, horror, etc will have to figure out the appropriate placement.
	- Some debate is needed on what the main genres should be, leaving others to be only verbally noted rather that being geo-plotted.)
	- The horizontal plotting will need some logic to connect the far East to the far West edges of the map into a globe (where the anti maridian would be).
	- Titles should be given land area using a formula similar to: (total viewership % + quality rating %) / Total size of Anime World
- Add a feature to the map showing users that are currently interacting and what titles they are rating, near real-time.

>This is where it goes completely beyond my experience level and into 3D frameworks like Unity or UnrealEngine.

- Use data sourced to make the 2D map to build a web and mobile compatible 3D globe similar to Google Earth.
    - The issue map makers have struggled with for centuries will play a part  here; how to show a land mass to the North or South and is the same size as near the equator.
	- User activity feature would show as satelites orbiting the region of titles they are rating with lines connecting to the land areas of the titles.
	- Land areas for titles would also have  skyscrapers based on the quality of their components. (e.g. Cweboy Bebop Land would have a skyscraper for Yoko Kanno's music since it's universally accepted as high quality and she has done the music for many other series.)
	- Additaonal building would include things like libraries, theatres, concert halls, etc. They would include either pop-up menues or a first-person internal environment showing information about the title, currated sample clips on youtube, where to stream videos or music online, etc.
	- Vegitation should be added to land areas based on the age of the title, how long it ran for, how recently viewers watched it, etc. (e.g. Samurai Pizza Cats should be a nearly desert-like region sinnce it aired in the 80's/90's and hasn't been on TV since and has no substantial current viewership like from DVD sales or online streaming views, but My Hero Academia and Demon Slayer should be lush jungles/forests.) This point is to encourage users to watch old forgotten titles and it willcause new vegitation to grow.
	- Offer a "plant a tree" option to decorate old titles' land areas that are deserving of a rewatch. Maybe limit number of seeds available to a user or have a dedicated park aside from wild vegitation where planted trees live for a a period of time or possibly forever. Park could grow in size as more trees are planted.
	- Make connections like roads or suspended highways between the components of different titles, whatever is visually pleasing. Could have littl epeople walking along these paths representing users that have explored new titles based on the similar components in recent weeks/months or over all time. Would be interesting to show the impact the app has made in introducing users to new titles because of the similarities they would otherwise never have known existed.
	- Maybe plot some titles under water. Think of a metric that makes sense for a land elevation in the negative, like violence content for example. Could be episode-specific so some areas are above ground and others are under water, lakes could be proceedurally generated to cover the appropriate perventage of the title's land area. Another metric that could produce continents and oceans would be density. If a ton of shonen titles end up very close together and a few are far away with few neighbors, that could determine where high land and deep oceans are.
