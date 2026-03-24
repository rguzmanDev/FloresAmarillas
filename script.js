document.addEventListener('DOMContentLoaded', () => {
    const bouquet = document.getElementById('bouquet');
    const sky = document.getElementById('sky');

    const isMobile = window.innerWidth <= 768;
    const fireflyCount = isMobile ? 15 : 40;

    for (let i = 0; i < fireflyCount; i++) {
        const firefly = document.createElement('div');
        firefly.className = 'firefly';
        firefly.style.left = `${Math.random() * 100}vw`;
        firefly.style.top = `${Math.random() * 100}vh`;
        firefly.style.setProperty('--dur', `${Math.random() * 3 + 2}s`);
        firefly.style.setProperty('--float-dur', `${Math.random() * 20 + 10}s`);

        const size = Math.random() * 2 + 1;
        firefly.style.width = `${size}px`;
        firefly.style.height = `${size}px`;

        sky.appendChild(firefly);
    }

    const flowerCount = isMobile ? 10 : 20;
    const flowers = [];

    for (let i = 0; i < flowerCount; i++) {
        const stemAngle = -30 + Math.random() * 60;

        const heightPercent = 0.35 + Math.random() * 0.45;
        const baseHeight = window.innerHeight * heightPercent;

        const scale = 0.45 + Math.random() * 0.45;

        const xOffset = (Math.random() - 0.5) * 60;

        flowers.push({
            xOffset,
            scale,
            baseHeight,
            stemAngle,
            delay: Math.random() * 1.5
        });
    }

    flowers.sort((a, b) => a.scale - b.scale);

    const fragment = document.createDocumentFragment();
    flowers.forEach((f, i) => createFlower(f, i, fragment));
    bouquet.appendChild(fragment);

    function createFlower(props, index, parentNode) {
        const wrapper = document.createElement('div');
        wrapper.className = 'flower-wrapper';

        wrapper.style.setProperty('--left', `calc(50% + ${props.xOffset}px)`);
        wrapper.style.setProperty('--scale', props.scale);
        wrapper.style.setProperty('--z-index', Math.floor(props.scale * 100));

        const stem = document.createElement('div');
        stem.className = 'stem';
        stem.style.setProperty('--stem-height', `${props.baseHeight}px`);
        stem.style.setProperty('--stem-w', `${4 + props.scale * 2}px`);
        stem.style.setProperty('--stem-angle', `${props.stemAngle}deg`);
        stem.style.setProperty('--delay', `${props.delay}s`);
        const numLeaves = Math.floor(Math.random() * 2) + 1;
        for (let j = 0; j < numLeaves; j++) {
            const leaf = document.createElement('div');
            const isLeft = Math.random() > 0.5;
            leaf.className = `leaf ${isLeft ? 'left' : 'right'}`;
            const leafPos = 10 + Math.random() * 50;
            leaf.style.bottom = `${leafPos}%`;

            const leafDelay = props.delay + 0.8 + Math.random() * 0.5;
            leaf.style.setProperty('--leaf-delay', `${leafDelay}s`);
            leaf.style.setProperty('--leaf-scale', 0.5 + Math.random() * 0.4);
            leaf.style.setProperty('--leaf-angle', `${(isLeft ? -1 : 1) * (15 + Math.random() * 30)}deg`);
            stem.appendChild(leaf);
        }

        const bloom = document.createElement('div');
        bloom.className = 'bloom';

        const layers = isMobile ? [
            { count: 14, scale: 1.0, tilt: '55deg', offset: 0 },
            { count: 10, scale: 0.85, tilt: '35deg', offset: 10 }
        ] : [
            { count: 18, scale: 1.0, tilt: '55deg', offset: 0 },
            { count: 14, scale: 0.85, tilt: '35deg', offset: 10 },
            { count: 10, scale: 0.7, tilt: '15deg', offset: 20 }
        ];

        layers.forEach((layer, layerIndex) => {
            for (let p = 0; p < layer.count; p++) {
                const petal = document.createElement('div');
                petal.className = 'petal';
                const rot = (360 / layer.count) * p + layer.offset;

                petal.style.setProperty('--rot', `${rot}deg`);
                petal.style.setProperty('--tilt', layer.tilt);
                petal.style.setProperty('--scale', layer.scale);

                const petalDelay = props.delay + 1.2 + (layerIndex * 0.2) + (p * 0.03);
                petal.style.setProperty('--petal-delay', `${petalDelay}s`);

                bloom.appendChild(petal);
            }
        });

        const center = document.createElement('div');
        center.className = 'center';
        center.style.setProperty('--center-delay', `${props.delay + 2.5}s`);

        bloom.appendChild(center);
        stem.appendChild(bloom);
        wrapper.appendChild(stem);
        parentNode.appendChild(wrapper);
    }
});
