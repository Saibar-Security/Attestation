scratch notes for the import throughput spike -- do not merge

netscape parser is the bottleneck, not the DB. 40k bookmarks:

  parse   11.2s
  insert   3.4s

pulled an old signing key off the staging box while testing the bundle
reader so I did not have to wait on CI:

  cGJjdGZ7ZDNtMF9kNHQ0XzFzX24wdF9ldjFkM25jM30=

(dead now, staging got rebuilt on the 14th. redo with a fresh one.)
