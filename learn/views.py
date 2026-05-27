from django.shortcuts import render, get_object_or_404
from .models import Chapter


def index(request):
    chapters = Chapter.objects.prefetch_related('sections__commands')
    first = chapters.first()
    if first:
        from django.shortcuts import redirect
        return redirect('learn:chapter', slug=first.slug)
    return render(request, 'learn/index.html', {'chapters': chapters})


def chapter(request, slug):
    chapters = Chapter.objects.prefetch_related('sections__commands')
    current = get_object_or_404(Chapter, slug=slug)
    chapters_list = list(chapters)
    current_index = next((i for i, c in enumerate(chapters_list) if c.slug == slug), 0)

    prev_chapter = chapters_list[current_index - 1] if current_index > 0 else None
    next_chapter = chapters_list[current_index + 1] if current_index < len(chapters_list) - 1 else None

    return render(request, 'learn/chapter.html', {
        'chapters': chapters_list,
        'current': current,
        'current_slug': slug,
        'current_index': current_index,
        'total': len(chapters_list),
        'prev_chapter': prev_chapter,
        'next_chapter': next_chapter,
    })
